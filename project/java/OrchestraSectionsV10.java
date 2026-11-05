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
  The sections a repository defines.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraSectionsV10  {

  private List<OrchestraSectionV10> fixrSection;
  private URI xmlBase;
  private Integer fixrLatestEp;


}