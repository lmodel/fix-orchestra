package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The ordered fields, groups and components of a message.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraMessageStructureV11  {

  private List<OrchestraStructureMemberV11> fixrMembers;
  private String fixrWhich;


}