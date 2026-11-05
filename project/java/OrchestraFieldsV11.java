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
  The fields a repository defines.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraFieldsV11  {

  private List<OrchestraFieldV11> fixrField;
  private OrchestraAnnotationV11 fixrAnnotation;
  private URI xmlBase;


}