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
  How a single use of a component, or every entry of a group, gets its values: the fields, components and groups it sets.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraBlockAssignmentV10  {

  private List<OrchestraStructureMemberV10> fixrMembers;


}